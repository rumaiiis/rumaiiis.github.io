document.addEventListener('DOMContentLoaded', function () {
    const input = document.getElementById('thm-search');
    const entries = Array.from(document.querySelectorAll('.thm-entry'));
    const emptyState = document.getElementById('thm-empty-state');
    const filters = Array.from(document.querySelectorAll('.archive-filter'));
    const groups = Array.from(document.querySelectorAll('.thm-entry-group'));
    let activeFilter = 'all';

    if (!input || entries.length === 0) {
        return;
    }

    function applyFilter() {
        const query = input.value.trim().toLowerCase();
        let visible = 0;

        entries.forEach(function (entry) {
            const haystack = [
                entry.dataset.name || '',
                entry.dataset.kind || '',
                entry.dataset.coverage || '',
                entry.dataset.group || '',
                entry.textContent || ''
            ].join(' ').toLowerCase();

            const queryMatch = query === '' || haystack.includes(query);
            const filterMatch = activeFilter === 'all' || entry.dataset.group === activeFilter || entry.dataset.kind === activeFilter || entry.dataset.coverage === activeFilter;
            const match = queryMatch && filterMatch;
            entry.hidden = !match;
            if (match) {
                visible += 1;
            }
        });

        groups.forEach(function (group) {
            const groupEntries = Array.from(group.querySelectorAll('.thm-entry'));
            const hasVisibleEntries = groupEntries.some(function (entry) {
                return !entry.hidden;
            });
            group.hidden = !hasVisibleEntries;
        });

        if (emptyState) {
            emptyState.hidden = visible !== 0;
        }
    }

    input.addEventListener('input', applyFilter);

    filters.forEach(function (button) {
        button.addEventListener('click', function () {
            activeFilter = button.dataset.filter || 'all';
            filters.forEach(function (item) {
                item.classList.toggle('is-active', item === button);
            });
            applyFilter();
        });
    });

    applyFilter();
});
